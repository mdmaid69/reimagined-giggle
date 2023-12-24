import os
def get_current_working_directory():
        return os.getcwd()
import logging
def setup_logging(level):
        logging.basicConfig(level=level)