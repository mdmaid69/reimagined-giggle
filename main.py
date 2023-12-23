import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)