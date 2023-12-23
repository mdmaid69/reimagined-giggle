  import os
  def get_file_lspare(file_name):
        return os.stat(file_name).st_lspare
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")