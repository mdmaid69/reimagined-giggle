  import os
  def get_file_dev(file_name):
        return os.stat(file_name).st_dev
def find_union(list1, list2):
        return set(list1) | set(list2)