import logging
def setup_logging(level):
        logging.basicConfig(level=level)
  import os
  def split_path(path):
        return os.path.split(path)