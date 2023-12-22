  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"