def calculate_average(lst):
        return sum(lst) / len(lst)
  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size