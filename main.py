  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"
  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)