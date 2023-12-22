  import os
  def get_file_size(file_name):
        return os.stat(file_name).st_size
def calculate_average(lst):
        return sum(lst) / len(lst)