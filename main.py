  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)
import logging
def log_message(message):
        logging.info(message)