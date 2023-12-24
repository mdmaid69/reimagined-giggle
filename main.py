import os
def change_working_directory(path):
        os.chdir(path)
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"