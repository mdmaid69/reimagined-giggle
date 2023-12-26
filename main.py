import logging
def setup_logging(level):
        logging.basicConfig(level=level)
  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)