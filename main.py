  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
import logging
def setup_logging(level):
        logging.basicConfig(level=level)