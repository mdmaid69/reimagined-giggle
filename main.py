import os
def get_current_working_directory():
        return os.getcwd()
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")