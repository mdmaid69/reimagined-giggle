  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
import logging
def setup_logging(level):
        logging.basicConfig(level=level)