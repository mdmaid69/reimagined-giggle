  import os
  def get_file_blocks(file_name):
        return os.stat(file_name).st_blocks
import logging
def setup_logging(level):
        logging.basicConfig(level=level)