  import os
  def delete_file(file_name):
        os.remove(file_name)
import logging
def setup_logging(level):
        logging.basicConfig(level=level)