import os
def list_files_in_directory(path):
        return os.listdir(path)
import logging
def setup_logging(level):
        logging.basicConfig(level=level)