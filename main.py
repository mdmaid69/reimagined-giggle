  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
import logging
def setup_logging(level):
        logging.basicConfig(level=level)