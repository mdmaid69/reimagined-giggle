  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
def find_difference(list1, list2):
        return set(list1) - set(list2)