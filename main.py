list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Difference:", set(list1) - set(list2))
  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)