  def reverse_list(lst):
        return lst[::-1]
  import os
  def get_file_birthtime_ns(file_name):
        return os.stat(file_name).st_birthtime_ns