  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime
  import time
  def wait_for_seconds(seconds):
        time.sleep(seconds)