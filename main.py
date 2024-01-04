  import time
  def wait_for_seconds(seconds):
        time.sleep(seconds)
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]