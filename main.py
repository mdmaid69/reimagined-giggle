  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags