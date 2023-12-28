import datetime
def get_current_datetime():
        return datetime.datetime.now()
  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)