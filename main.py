  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size
import datetime
def get_current_datetime():
        return datetime.datetime.now()