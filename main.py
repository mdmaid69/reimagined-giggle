import os
def get_file_size(filename):
        return os.path.getsize(filename)
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"