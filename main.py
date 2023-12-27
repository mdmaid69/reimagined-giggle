  import os
  def get_file_size(file_name):
        return os.stat(file_name).st_size
import logging
def setup_logging(level):
        logging.basicConfig(level=level)