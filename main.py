import logging
def setup_logging(level):
        logging.basicConfig(level=level)
  import os
  def get_current_directory():
        return os.getcwd()