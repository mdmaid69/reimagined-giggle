  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"
  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)