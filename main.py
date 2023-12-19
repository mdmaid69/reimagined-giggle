  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"