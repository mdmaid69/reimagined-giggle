  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
  def count_elements(lst):
        return len(lst)