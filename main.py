  import os
  def get_file_number_of_links(file_name):
        return os.stat(file_name).st_nlink
def find_union(list1, list2):
        return set(list1) | set(list2)