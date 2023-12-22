  import os
  def get_file_blocks_allocated(file_name):
        return os.stat(file_name).st_blocks
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")