  import os
  def get_file_size(file_name):
        return os.stat(file_name).st_size
import logging
def log_message(message):
        logging.info(message)