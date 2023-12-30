  import os
  def split_path(path):
        return os.path.split(path)
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Common elements:", set(list1) & set(list2))