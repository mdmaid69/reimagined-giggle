import datetime
def get_current_date():
        return datetime.date.today()
  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)