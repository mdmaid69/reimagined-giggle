  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"