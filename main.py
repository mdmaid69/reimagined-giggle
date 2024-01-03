  import time
  def wait_for_seconds(seconds):
        time.sleep(seconds)
  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)