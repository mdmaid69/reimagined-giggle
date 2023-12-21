import logging
def log_message(message):
        logging.info(message)
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)