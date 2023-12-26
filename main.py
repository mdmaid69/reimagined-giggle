  import time
  def wait_for_seconds(seconds):
        time.sleep(seconds)
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)