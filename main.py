  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Common elements:", set(list1) & set(list2))