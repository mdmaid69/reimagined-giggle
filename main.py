  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
import logging
def log_message(message):
        logging.info(message)