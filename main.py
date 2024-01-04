  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"
  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)