  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
def find_difference(list1, list2):
        return set(list1) - set(list2)