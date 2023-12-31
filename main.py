import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"