  import os
  def get_file_ctime(file_name):
        return os.stat(file_name).st_ctime
import logging
def log_message(message):
        logging.info(message)