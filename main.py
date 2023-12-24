import logging
def setup_logging(level):
        logging.basicConfig(level=level)
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)