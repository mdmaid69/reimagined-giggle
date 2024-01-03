  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino
  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"