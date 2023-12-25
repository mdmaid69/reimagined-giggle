  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)