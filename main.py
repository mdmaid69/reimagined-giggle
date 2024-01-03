import logging
def log_message(message):
        logging.info(message)
  import os
  def get_base_name(path):
        return os.path.basename(path)