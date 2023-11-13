import os
import platform
from contextlib import contextmanager
from datetime import datetime

import pytz
import requests
from snowplow_tracker import Emitter, StructuredEvent, Tracker
from snowplow_tracker import logger as sp_logger

sp_logger.setLevel(60)  # turn off snowplow logging

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
        sp_logger.info(f"Failed to track the event: num_ok={num_ok}, unsent={unsent}")

    def _log_request(self, request, payload):
        sp_logger.info(f"Sending {request} request to {self.endpoint}...")
        sp_logger.debug(f"Payload: {payload}")

    def _log_result(self, request, status_code):
        msg = f"{request} request finished with status code: {status_code}"
        if self.is_good_status_code(status_code):
            sp_logger.info(msg)
        else:
            sp_logger.warning(msg)

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


class User:
    def __init__(self) -> None:
        self.do_not_track = True
        self.run_started_at = datetime.now(tz=pytz.utc)

    def state(self):
        return "do not track" if self.do_not_track else "tracking"

    def disable_tracking(self):
        self.do_not_track = True

    def enable_tracking(self):
        self.do_not_track = False


class SpTracker:
    def __init__(self) -> None:
        self.tracker = Tracker(
            namespace="snowplow_tracker",
            app_id="diqu",
            emitters=[TimeoutEmitter()],
        )
        self.user = self.get_user()

    def get_user(self):
        send_anonymous_usage_stats = True
        if os.getenv("DO_NOT_TRACK", "").lower() in ("1", "t", "true", "y", "yes"):
            send_anonymous_usage_stats = False

        if send_anonymous_usage_stats:
            active_user = User()
            try:
                active_user.enable_tracking()
                return active_user
            except Exception:
                return User()

        return User()

    def track(self, **kwargs):
        if self.user.do_not_track:
            return
        else:
            try:
                self.tracker.track(StructuredEvent(**kwargs))
            except Exception:
                return False
        return True

    def get_platform_context(self):
        return {
            "platform": platform.platform(),
            "python": platform.python_implementation(),
            "python_version": platform.python_version(),
        }

    def track_invocation_start(self, invocation_context):
        assert (
            self.user is not None
        ), "Cannot track invocation end when active user is None"
        data = {"invocation_context": invocation_context}
        data.update(self.get_platform_context())

        return self.track(
            category="diqu",
            action="invocation",
            label="start",
            property_=str(data),
        )

    def track_invocation_end(self, invocation_context, result_type=None):
        assert (
            self.user is not None
        ), "Cannot track invocation end when active user is None"
        data = {"invocation_context": invocation_context, "result_type": result_type}
        data.update(self.get_platform_context())

        return self.track(
            category="diqu",
            action="invocation",
            label="end",
            property_=str(data),
        )

    def flush(self):
        try:
            self.tracker.flush()
        except Exception:
            pass


@contextmanager
def track_run(run_command=None, params=None, version=None):
    tracker = SpTracker()
    invocation_context = {
        "command": run_command,
        "params": params,
        "version": version,
    }
    tracker.track_invocation_start(invocation_context)
    try:
        yield
        tracker.track_invocation_end(invocation_context, result_type="ok")
    except Exception:
        tracker.track_invocation_end(invocation_context, result_type="error")
        raise
    finally:
        tracker.flush()
