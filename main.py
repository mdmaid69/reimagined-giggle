import logging
def log_message(message):
        logging.info(message)
  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime