  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())