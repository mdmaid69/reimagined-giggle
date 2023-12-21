  import os
  def get_file_birthtime_ns(file_name):
        return os.stat(file_name).st_birthtime_ns
  import time
  def wait_for_seconds(seconds):
        time.sleep(seconds)