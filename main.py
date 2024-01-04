  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
def find_difference(list1, list2):
        return set(list1) - set(list2)