  import os
  def get_file_birthtime_ns(file_name):
        return os.stat(file_name).st_birthtime_ns
import logging
def setup_logging(level):
        logging.basicConfig(level=level)