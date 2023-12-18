  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())