  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)