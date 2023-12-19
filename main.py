import logging
def setup_logging(level):
        logging.basicConfig(level=level)
  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime