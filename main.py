  import os
  def split_path(path):
        return os.path.split(path)
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"