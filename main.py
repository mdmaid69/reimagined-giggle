import logging
def log_message(message):
        logging.info(message)
  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)