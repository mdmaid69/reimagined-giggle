  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
def find_common_elements(list1, list2):
        return set(list1) & set(list2)