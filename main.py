  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)
  import datetime
  def get_current_date():
        return datetime.datetime.now().date()