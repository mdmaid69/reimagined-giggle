import logging
def log_message(message):
        logging.info(message)
import os
def remove_directory(path):
        os.rmdir(path)