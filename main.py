  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
import logging
def setup_logging(level):
        logging.basicConfig(level=level)