  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"