import logging
def log_message(message):
        logging.info(message)
import os
def get_file_size(filename):
        return os.path.getsize(filename)