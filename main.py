import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)