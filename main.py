import datetime
def get_current_datetime():
        return datetime.datetime.now()
  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare