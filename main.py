  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink
  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"