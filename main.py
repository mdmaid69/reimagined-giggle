  import os
  def get_file_gid(file_name):
        return os.stat(file_name).st_gid
import datetime
def get_current_datetime():
        return datetime.datetime.now()