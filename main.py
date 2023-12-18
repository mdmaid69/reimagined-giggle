  import os
  def get_file_blocks(file_name):
        return os.stat(file_name).st_blocks
  import time
  def wait_for_seconds(seconds):
        time.sleep(seconds)