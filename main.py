import os
def change_working_directory(path):
        os.chdir(path)
  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"