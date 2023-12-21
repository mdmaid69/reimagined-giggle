  import os
  def get_directory_name(path):
        return os.path.dirname(path)
import logging
def setup_logging(level):
        logging.basicConfig(level=level)