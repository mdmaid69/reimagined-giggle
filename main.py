  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
def find_union(list1, list2):
        return set(list1) | set(list2)