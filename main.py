import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
import logging
def setup_logging(level):
        logging.basicConfig(level=level)