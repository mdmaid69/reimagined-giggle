  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
import logging
def log_message(message):
        logging.info(message)