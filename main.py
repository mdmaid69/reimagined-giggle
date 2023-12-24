import datetime
def get_current_date():
        return datetime.date.today()
  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime