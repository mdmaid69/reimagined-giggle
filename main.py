  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
import logging
def log_message(message):
        logging.info(message)