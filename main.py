  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
import logging
def setup_logging(level):
        logging.basicConfig(level=level)