import logging
def log_message(message):
        logging.info(message)
import os
def change_working_directory(path):
        os.chdir(path)