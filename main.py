  import os
  def get_file_dev(file_name):
        return os.stat(file_name).st_dev
import time
def get_current_time():
        return time.time()