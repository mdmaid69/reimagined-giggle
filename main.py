  import os
  def delete_file(file_name):
        os.remove(file_name)
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())