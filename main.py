import logging
def log_message(message):
        logging.info(message)
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)