  import os
  def get_file_atime_ns(file_name):
        return os.stat(file_name).st_atime_ns
  import time
  def wait_for_seconds(seconds):
        time.sleep(seconds)