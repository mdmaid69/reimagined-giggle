  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime
def find_common_elements(list1, list2):
        return set(list1) & set(list2)