def calculate_average(lst):
        return sum(lst) / len(lst)
  import os
  def get_file_mode(file_name):
        return os.stat(file_name).st_mode