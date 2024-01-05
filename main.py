  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags
def count_elements(lst):
        return len(lst)