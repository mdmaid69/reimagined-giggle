  import os
  def get_file_gid(file_name):
        return os.stat(file_name).st_gid
def calculate_average(lst):
        return sum(lst) / len(lst)