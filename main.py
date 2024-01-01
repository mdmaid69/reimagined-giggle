  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)
  def reverse_list(lst):
        return lst[::-1]