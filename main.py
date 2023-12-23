import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)