  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)
  def remove_duplicates(lst):
        return list(set(lst))