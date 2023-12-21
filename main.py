  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)