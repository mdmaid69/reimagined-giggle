  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)