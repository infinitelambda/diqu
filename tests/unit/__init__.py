import os

from diqu.utils.log import logger

logger.propagate = True
os.environ["DO_NOT_TRACK"] = "1"
