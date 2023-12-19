  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino
  import datetime
  def get_current_date():
        return datetime.datetime.now().date()