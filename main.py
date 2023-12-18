import logging
def log_message(message):
        logging.info(message)
  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]