  import os
  def get_file_uid(file_name):
        return os.stat(file_name).st_uid
import datetime
def get_current_datetime():
        return datetime.datetime.now()