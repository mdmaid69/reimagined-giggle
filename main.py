import logging
def setup_logging(level):
        logging.basicConfig(level=level)
  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)