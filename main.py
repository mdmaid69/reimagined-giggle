import logging
def log_message(message):
        logging.info(message)
import glob
def find_files(pattern):
        return glob.glob(pattern)