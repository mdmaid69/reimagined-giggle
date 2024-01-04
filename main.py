  import os
  def get_file_inode(file_name):
        return os.stat(file_name).st_ino
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"