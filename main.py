  import os
  def get_file_ctime_ns(file_name):
        return os.stat(file_name).st_ctime_ns
  def remove_duplicates(lst):
        return list(set(lst))