  import os
  def get_file_mode(file_name):
        return os.stat(file_name).st_mode
import logging
def setup_logging(level):
        logging.basicConfig(level=level)