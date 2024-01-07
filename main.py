  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags
import logging
def setup_logging(level):
        logging.basicConfig(level=level)