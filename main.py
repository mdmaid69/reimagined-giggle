import logging
def setup_logging(level):
        logging.basicConfig(level=level)
import glob
def find_files(pattern):
        return glob.glob(pattern)