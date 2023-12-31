  import time
  def wait_for_seconds(seconds):
        time.sleep(seconds)
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)