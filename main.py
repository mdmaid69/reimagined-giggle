import os
def get_current_working_directory():
        return os.getcwd()
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"