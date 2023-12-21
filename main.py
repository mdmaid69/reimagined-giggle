  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink
import logging
def log_message(message):
        logging.info(message)