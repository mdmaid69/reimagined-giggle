  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino
def calculate_average(lst):
        return sum(lst) / len(lst)