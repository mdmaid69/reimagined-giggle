def find_common_elements(list1, list2):
        return set(list1) & set(list2)
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)