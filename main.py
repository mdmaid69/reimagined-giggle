import os
def get_file_size(filename):
        return os.path.getsize(filename)
  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"