import time
def get_current_time():
        return time.ctime()
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]