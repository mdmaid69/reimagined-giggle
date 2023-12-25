  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime
import datetime
def get_current_datetime():
        return datetime.datetime.now()