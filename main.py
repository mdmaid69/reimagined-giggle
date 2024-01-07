  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink
  def sort_list(lst):
        return sorted(lst)