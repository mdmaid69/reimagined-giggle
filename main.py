import logging
def log_message(message):
        logging.info(message)
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)