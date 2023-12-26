  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
import logging
def log_message(message):
        logging.info(message)