import os
def get_current_working_directory():
        return os.getcwd()
  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"