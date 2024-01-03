def find_union(list1, list2):
        return set(list1) | set(list2)
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)