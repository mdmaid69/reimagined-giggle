  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
def reverse_list(lst):
        return lst[::-1]