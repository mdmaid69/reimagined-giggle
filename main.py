import platform
def get_os_info():
        return platform.uname()
import logging
def log_message(message):
        logging.info(message)