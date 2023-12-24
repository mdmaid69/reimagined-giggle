import logging
def setup_logging(level):
        logging.basicConfig(level=level)
  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)