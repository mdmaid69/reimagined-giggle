def calculate_average(lst):
        return sum(lst) / len(lst)
  import os
  def get_file_uid(file_name):
        return os.stat(file_name).st_uid