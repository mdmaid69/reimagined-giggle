import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)