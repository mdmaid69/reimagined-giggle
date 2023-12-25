  import os
  def get_file_dev(file_name):
        return os.stat(file_name).st_dev
  import time
  def wait_for_seconds(seconds):
        time.sleep(seconds)