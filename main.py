import platform
def get_python_version():
        return platform.python_version()
import logging
def log_message(message):
        logging.info(message)