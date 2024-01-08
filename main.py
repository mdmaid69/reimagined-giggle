  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
def find_common_elements(list1, list2):
        return set(list1) & set(list2)