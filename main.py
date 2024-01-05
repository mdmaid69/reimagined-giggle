  import os
  def get_file_gid(file_name):
        return os.stat(file_name).st_gid
import logging
def log_message(message):
        logging.info(message)