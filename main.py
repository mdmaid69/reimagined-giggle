import logging
def log_message(message):
        logging.info(message)
  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)