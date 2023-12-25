import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"