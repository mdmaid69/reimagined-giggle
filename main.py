  import os
  def get_file_device(file_name):
        return os.stat(file_name).st_dev
import logging
def setup_logging(level):
        logging.basicConfig(level=level)