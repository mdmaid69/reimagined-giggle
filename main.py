  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime
import logging
def log_message(message):
        logging.info(message)