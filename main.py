  import os
  def get_base_name(path):
        return os.path.basename(path)
  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"