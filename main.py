  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
import time
def get_current_time():
        return time.time()