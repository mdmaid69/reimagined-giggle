  def remove_duplicates(lst):
        return list(set(lst))
  import os
  def get_file_gid(file_name):
        return os.stat(file_name).st_gid