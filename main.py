  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)
  import datetime
  def get_current_date():
        return datetime.datetime.now().date()