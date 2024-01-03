  import os
  def get_current_directory():
        return os.getcwd()
  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"