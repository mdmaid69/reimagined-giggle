import logging
def setup_logging(level):
        logging.basicConfig(level=level)
import os
def change_working_directory(path):
        os.chdir(path)