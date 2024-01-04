  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags
import datetime
def get_current_datetime():
        return datetime.datetime.now()