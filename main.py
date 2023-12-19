  import os
  def get_current_directory():
        return os.getcwd()
import logging
def setup_logging(level):
        logging.basicConfig(level=level)