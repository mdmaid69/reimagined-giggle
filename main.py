list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Common elements:", set(list1) & set(list2))
  import os
  def get_base_name(path):
        return os.path.basename(path)