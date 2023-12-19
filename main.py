  import os
  def delete_file(file_name):
        os.remove(file_name)
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")