  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
  def count_elements(lst):
        return len(lst)