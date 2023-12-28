  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")