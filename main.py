  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"