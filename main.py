  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")