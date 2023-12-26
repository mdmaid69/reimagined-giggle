  import os
  def get_file_lspare(file_name):
        return os.stat(file_name).st_lspare
import logging
def setup_logging(level):
        logging.basicConfig(level=level)