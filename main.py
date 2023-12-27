  import os
  def get_file_birthtime(file_name):
        return os.stat(file_name).st_birthtime
  import time
  def wait_for_seconds(seconds):
        time.sleep(seconds)