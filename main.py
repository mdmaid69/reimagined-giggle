  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)
  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"