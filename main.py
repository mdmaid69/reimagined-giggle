  import os
  def get_file_birthtime(file_name):
        return os.stat(file_name).st_birthtime
  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"