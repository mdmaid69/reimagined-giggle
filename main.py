  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"