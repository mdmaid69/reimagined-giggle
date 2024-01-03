  import os
  def get_base_name(path):
        return os.path.basename(path)
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"