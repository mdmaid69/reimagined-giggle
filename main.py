  import os
  def get_directory_name(path):
        return os.path.dirname(path)
def find_difference(list1, list2):
        return set(list1) - set(list2)