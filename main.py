import logging
def log_message(message):
        logging.info(message)
  import os
  def delete_file(file_name):
        os.remove(file_name)