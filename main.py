  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
  def reverse_list(lst):
        return lst[::-1]