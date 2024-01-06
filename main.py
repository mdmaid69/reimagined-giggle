  import os
  def get_directory_name(path):
        return os.path.dirname(path)
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())