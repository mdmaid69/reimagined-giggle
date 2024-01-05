  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags
import time
def get_current_time():
        return time.time()