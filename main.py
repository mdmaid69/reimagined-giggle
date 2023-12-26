  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"