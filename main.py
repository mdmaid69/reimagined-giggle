  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())