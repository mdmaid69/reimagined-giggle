  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"