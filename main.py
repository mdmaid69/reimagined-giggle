  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink
def find_difference(list1, list2):
        return set(list1) - set(list2)