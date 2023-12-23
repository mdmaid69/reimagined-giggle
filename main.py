  import os
  def get_base_name(path):
        return os.path.basename(path)
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")