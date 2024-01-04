  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)
import logging
def setup_logging(level):
        logging.basicConfig(level=level)