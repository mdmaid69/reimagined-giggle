  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Common elements:", set(list1) & set(list2))