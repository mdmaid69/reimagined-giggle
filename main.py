  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"