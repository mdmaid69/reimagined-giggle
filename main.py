import logging
def log_message(message):
        logging.info(message)
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)