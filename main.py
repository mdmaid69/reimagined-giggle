  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
import time
def get_current_time():
        return time.time()