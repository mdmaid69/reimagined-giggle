  import os
  def get_file_group(file_name):
        return os.stat(file_name).st_gid
  import datetime
  def get_current_date():
        return datetime.datetime.now().date()