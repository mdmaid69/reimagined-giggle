import platform
def get_python_version():
        return platform.python_version()
import logging
def setup_logging(level):
        logging.basicConfig(level=level)