import logging
def setup_logging(level):
        logging.basicConfig(level=level)
import platform
def get_python_version():
        return platform.python_version()