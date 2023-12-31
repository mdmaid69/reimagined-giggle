  def sort_list(lst):
        return sorted(lst)
  import os
  def get_file_group(file_name):
        return os.stat(file_name).st_gid