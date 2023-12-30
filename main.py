  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
import logging
def log_message(message):
        logging.info(message)