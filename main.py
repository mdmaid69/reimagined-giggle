  import os
  def split_path(path):
        return os.path.split(path)
  import datetime
  def get_current_date():
        return datetime.datetime.now().date()