import logging
def log_message(message):
        logging.info(message)
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)