  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
def find_difference(list1, list2):
        return set(list1) - set(list2)