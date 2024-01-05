import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)