  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
import logging
def log_message(message):
        logging.info(message)