def calculate_average(lst):
        return sum(lst) / len(lst)
  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize