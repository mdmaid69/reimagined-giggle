  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())