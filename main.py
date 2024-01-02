import logging
def setup_logging(level):
        logging.basicConfig(level=level)
import os
def remove_directory(path):
        os.rmdir(path)