import logging
def setup_logging(level):
        logging.basicConfig(level=level)
import platform
def get_os_info():
        return platform.uname()