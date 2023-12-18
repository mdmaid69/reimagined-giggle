  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags
def find_difference(list1, list2):
        return set(list1) - set(list2)