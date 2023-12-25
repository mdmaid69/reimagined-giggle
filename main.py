import logging
def log_message(message):
        logging.info(message)
import shutil
def delete_directory(path):
        shutil.rmtree(path)