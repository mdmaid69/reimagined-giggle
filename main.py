  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)
  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"