  import os
  def get_file_dev(file_name):
        return os.stat(file_name).st_dev
def find_min(lst):
        return min(lst)