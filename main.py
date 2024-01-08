import logging
def log_message(message):
        logging.info(message)
import os
def list_files_in_directory(path):
        return os.listdir(path)