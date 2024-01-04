  import os
  def get_file_ctime(file_name):
        return os.stat(file_name).st_ctime
import datetime
def get_current_datetime():
        return datetime.datetime.now()