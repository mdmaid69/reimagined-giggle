  import os
  def get_file_inode(file_name):
        return os.stat(file_name).st_ino
import logging
def log_message(message):
        logging.info(message)