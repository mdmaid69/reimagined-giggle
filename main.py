  import os
  def get_file_ctime_ns(file_name):
        return os.stat(file_name).st_ctime_ns
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"