  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
  import time
  def wait_for_seconds(seconds):
        time.sleep(seconds)