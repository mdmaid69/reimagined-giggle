  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"