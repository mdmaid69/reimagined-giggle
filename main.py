  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
def find_difference(list1, list2):
        return set(list1) - set(list2)