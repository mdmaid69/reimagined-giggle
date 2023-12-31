import logging
def setup_logging(level):
        logging.basicConfig(level=level)
import os
def get_current_working_directory():
        return os.getcwd()