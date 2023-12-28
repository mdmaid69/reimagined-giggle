  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)