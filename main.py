  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize
  import datetime
  def get_current_date():
        return datetime.datetime.now().date()