  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize
import logging
def log_message(message):
        logging.info(message)