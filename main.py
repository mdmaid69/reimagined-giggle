  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
  import datetime
  def get_current_date():
        return datetime.datetime.now().date()