  import os
  def get_file_dev(file_name):
        return os.stat(file_name).st_dev
  def remove_duplicates(lst):
        return list(set(lst))