  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
  def remove_duplicates(lst):
        return list(set(lst))