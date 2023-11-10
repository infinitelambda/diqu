import platform
from datetime import datetime
from typing import Optional

import pytz
import requests
from snowplow_tracker import Emitter, StructuredEvent, Tracker
from diqu.utils.log import logger

COLLECTOR_URL = "com-infinitelambda1-saas1.collector.snplow.net"
COLLECTOR_PROTOCOL = "https"


class TimeoutEmitter(Emitter):
    def __init__(self) -> None:
        super().__init__(
            COLLECTOR_URL,
            protocol=COLLECTOR_PROTOCOL,
            buffer_capacity=30,
            on_failure=self.handle_failure,
            method="post",
            byte_limit=None,  # don't set this.
        )

    @staticmethod
    def handle_failure(num_ok, unsent):
        disable_tracking()

    def _log_request(self, request, payload):
        logger.info(f"Sending {request} request to {self.endpoint}...")
        logger.debug(f"Payload: {payload}")

    def _log_result(self, request, status_code):
        msg = f"{request} request finished with status code: {status_code}"
        if self.is_good_status_code(status_code):
            logger.info(msg)
        else:
            logger.warning(msg)

    def http_post(self, payload):
        self._log_request("POST", payload)
        r = requests.post(
            self.endpoint,
            data=payload,
            headers={"content-type": "application/json; charset=utf-8"},
            timeout=5.0,
        )
        self._log_result("POST", r.status_code)
        return r

    def http_get(self, payload):
        self._log_request("GET", payload)
        r = requests.get(self.endpoint, params=payload, timeout=5.0)
        self._log_result("GET", r.status_code)
        return r


e = TimeoutEmitter()
tracker = Tracker(
    namespace="snowplow_tracker",
    app_id="diqu",
    emitters=[e],
)


class User:
    def __init__(self) -> None:
        self.do_not_track = True
        self.run_started_at = datetime.now(tz=pytz.utc)

    def state(self):
        return "do not track" if self.do_not_track else "tracking"

    def disable_tracking(self):
        self.do_not_track = True

    def initialize(self):
        self.do_not_track = False


active_user: Optional[User] = None


def get_platform_context():
    return {
        "platform": platform.platform(),
        "python": platform.python_version(),
        "python_version": platform.python_implementation(),
    }


def track(user, **kwargs):
    if user.do_not_track:
        return
    else:
        try:
            struct_event = StructuredEvent(**kwargs)
            tracker.track(struct_event)
        except Exception:
            pass


def flush():
    try:
        tracker.flush()
    except Exception:
        pass


def disable_tracking():
    global active_user
    if active_user is not None:
        active_user.disable_tracking()
    else:
        active_user = User(None)


def track_invocation_start(invocation_context):
    assert (
        active_user is not None
    ), "Cannot track invocation end when active user is None"
    data = {"invocation_context": invocation_context}
    data.update(get_platform_context())

    track(
        active_user,
        category="diqu",
        action="invocation",
        label="start",
        property_=str(data),
    )


def track_invocation_end(invocation_context, result_type=None):
    assert (
        active_user is not None
    ), "Cannot track invocation end when active user is None"

    data = {"invocation_context": invocation_context, "result_type": result_type}
    data.update(get_platform_context())

    track(
        active_user,
        category="diqu",
        action="invocation",
        label="end",
        property_=str(data),
    )


def initialize_user_tracking(send_anonymous_usage_stats: bool = False):
    global active_user
    if send_anonymous_usage_stats:
        active_user = User()
        try:
            active_user.initialize()
        except Exception:
            active_user = User(None)
    else:
        active_user = User(None)


def track_run(run_command=None, params=None, version=None):
    invocation_context = {"command": run_command, "params": params, "version": version}

    track_invocation_start(invocation_context)
    try:
        track_invocation_end(invocation_context, result_type="ok")
    except Exception:
        track_invocation_end(invocation_context, result_type="error")
    finally:
        flush()
