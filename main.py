  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
  import os
  def get_directory_name(path):
        return os.path.dirname(path)