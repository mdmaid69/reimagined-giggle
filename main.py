import glob
def find_files(pattern):
        return glob.glob(pattern)
import logging
def log_message(message):
        logging.info(message)