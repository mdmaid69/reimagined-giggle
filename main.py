  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
import time
def get_current_time():
        return time.time()