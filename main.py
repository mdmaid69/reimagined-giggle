import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
import logging
def setup_logging(level):
        logging.basicConfig(level=level)