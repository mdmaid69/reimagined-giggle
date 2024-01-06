  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
import time
def wait_for_seconds(seconds):
        time.sleep(seconds)