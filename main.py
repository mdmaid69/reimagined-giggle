  import os
  def get_file_group(file_name):
        return os.stat(file_name).st_gid
import logging
def setup_logging(level):
        logging.basicConfig(level=level)