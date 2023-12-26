  import os
  def split_path(path):
        return os.path.split(path)
  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"