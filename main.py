import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)