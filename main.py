  import time
  def wait_for_seconds(seconds):
        time.sleep(seconds)
  import os
  def get_file_ctime(file_name):
        return os.stat(file_name).st_ctime