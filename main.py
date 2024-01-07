import logging
def log_message(message):
        logging.info(message)
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]