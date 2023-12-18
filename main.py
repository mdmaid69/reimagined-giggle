  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
import time
def wait_for_seconds(seconds):
        time.sleep(seconds)