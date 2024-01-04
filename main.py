  import os
  def get_file_atime_ns(file_name):
        return os.stat(file_name).st_atime_ns
import logging
def setup_logging(level):
        logging.basicConfig(level=level)