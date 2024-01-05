import platform
def get_python_version():
        return platform.python_version()
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")