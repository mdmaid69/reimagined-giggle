  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Common elements:", set(list1) & set(list2))