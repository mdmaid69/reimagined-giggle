  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"