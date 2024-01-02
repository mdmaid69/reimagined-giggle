  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"
  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags