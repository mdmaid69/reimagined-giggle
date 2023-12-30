import logging
def log_message(message):
        logging.info(message)
  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)