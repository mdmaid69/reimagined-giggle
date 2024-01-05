  import os
  def get_file_group(file_name):
        return os.stat(file_name).st_gid
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")