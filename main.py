  import os
  def get_base_name(path):
        return os.path.basename(path)
def find_union(list1, list2):
        return set(list1) | set(list2)