import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)