import logging
def log_message(message):
        logging.info(message)
import shutil
def move_file(src, dst):
        shutil.move(src, dst)