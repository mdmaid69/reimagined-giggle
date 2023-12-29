  import time
  def wait_for_seconds(seconds):
        time.sleep(seconds)
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)