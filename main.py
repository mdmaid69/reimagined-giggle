  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
import logging
def setup_logging(level):
        logging.basicConfig(level=level)