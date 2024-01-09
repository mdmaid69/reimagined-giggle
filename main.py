  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"