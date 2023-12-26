  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)