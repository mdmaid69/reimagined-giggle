  import os
  def get_current_working_directory():
        return os.getcwd()
def find_difference(list1, list2):
        return set(list1) - set(list2)