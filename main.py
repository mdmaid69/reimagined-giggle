import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
  import time
  def wait_for_seconds(seconds):
        time.sleep(seconds)