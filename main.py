  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)
  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"