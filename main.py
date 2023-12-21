  import os
  def split_path(path):
        return os.path.split(path)
def find_common_elements(list1, list2):
        return set(list1) & set(list2)