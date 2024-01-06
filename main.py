  import os
  def delete_file(file_name):
        os.remove(file_name)
def find_difference(list1, list2):
        return set(list1) - set(list2)