  import time
  def wait_for_seconds(seconds):
        time.sleep(seconds)
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)