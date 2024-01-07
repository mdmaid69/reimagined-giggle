def find_common_elements(list1, list2):
        return set(list1) & set(list2)
  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare