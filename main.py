  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
import time
def get_current_time():
        return time.time()