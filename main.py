import logging
def log_message(message):
        logging.info(message)
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)