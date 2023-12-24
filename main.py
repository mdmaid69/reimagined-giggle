import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
import platform
def get_os_info():
        return platform.uname()