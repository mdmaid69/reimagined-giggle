  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags
  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"