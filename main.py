def sort_list(lst):
        return sorted(lst)
  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino