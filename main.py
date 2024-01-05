  import os
  def get_base_name(path):
        return os.path.basename(path)
import logging
def setup_logging(level):
        logging.basicConfig(level=level)