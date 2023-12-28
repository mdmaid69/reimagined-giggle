import logging
def log_message(message):
        logging.info(message)
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)