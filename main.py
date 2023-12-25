  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]
def find_difference(list1, list2):
        return set(list1) - set(list2)