import datetime
def get_current_datetime():
        return datetime.datetime.now()
  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)