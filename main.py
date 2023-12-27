  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
import time
def wait_for_seconds(seconds):
        time.sleep(seconds)