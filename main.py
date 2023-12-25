import shutil
def delete_directory(path):
        shutil.rmtree(path)
import logging
def setup_logging(level):
        logging.basicConfig(level=level)