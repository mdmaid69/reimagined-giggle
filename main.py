  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
def find_difference(list1, list2):
        return set(list1) - set(list2)