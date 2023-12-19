  import time
  def wait_for_seconds(seconds):
        time.sleep(seconds)
import os
def get_file_size(filename):
        return os.path.getsize(filename)