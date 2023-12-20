  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"
  import os
  def get_directory_name(path):
        return os.path.dirname(path)