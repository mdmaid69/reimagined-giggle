  import os
  def split_path(path):
        return os.path.split(path)
  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"