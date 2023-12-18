  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)
def find_common_elements(list1, list2):
        return set(list1) & set(list2)