  import os
  def get_file_permissions(file_name):
        return os.stat(file_name).st_mode
  import time
  def wait_for_seconds(seconds):
        time.sleep(seconds)