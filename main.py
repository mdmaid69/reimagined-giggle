  import os
  def get_file_birthtime(file_name):
        return os.stat(file_name).st_birthtime
  def remove_duplicates(lst):
        return list(set(lst))