  def remove_duplicates(lst):
        return list(set(lst))
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)