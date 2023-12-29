import datetime
def get_current_datetime():
        return datetime.datetime.now()
  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)