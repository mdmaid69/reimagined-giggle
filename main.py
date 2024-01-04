  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"