  import os
  def get_file_permissions(file_name):
        return os.stat(file_name).st_mode
import logging
def log_message(message):
        logging.info(message)