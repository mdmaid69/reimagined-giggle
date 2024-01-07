import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]