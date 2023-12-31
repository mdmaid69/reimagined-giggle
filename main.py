  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
import logging
def setup_logging(level):
        logging.basicConfig(level=level)