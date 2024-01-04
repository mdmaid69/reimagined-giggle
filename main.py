  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Common elements:", set(list1) & set(list2))