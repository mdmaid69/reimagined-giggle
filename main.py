import time
def get_current_time():
        return time.time()
  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]