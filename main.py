  import os
  def get_file_blocks_allocated(file_name):
        return os.stat(file_name).st_blocks
import logging
def log_message(message):
        logging.info(message)