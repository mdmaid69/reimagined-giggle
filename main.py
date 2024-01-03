import logging
def log_message(message):
        logging.info(message)
  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)