  import os
  def get_file_birthtime(file_name):
        return os.stat(file_name).st_birthtime
import logging
def setup_logging(level):
        logging.basicConfig(level=level)