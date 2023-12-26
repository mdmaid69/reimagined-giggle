  import time
  def wait_for_seconds(seconds):
        time.sleep(seconds)
  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)