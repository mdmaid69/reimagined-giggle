import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"