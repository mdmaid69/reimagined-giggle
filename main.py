import os
def get_file_size(filename):
        return os.path.getsize(filename)
import logging
def setup_logging(level):
        logging.basicConfig(level=level)