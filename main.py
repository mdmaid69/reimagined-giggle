import os
def remove_directory(path):
        os.rmdir(path)
  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"