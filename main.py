  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
  import datetime
  def get_current_date():
        return datetime.datetime.now().date()