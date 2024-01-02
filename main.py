  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())