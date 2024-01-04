  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)
import logging
def setup_logging(level):
        logging.basicConfig(level=level)