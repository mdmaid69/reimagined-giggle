import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)