  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)
def find_common_elements(list1, list2):
        return set(list1) & set(list2)