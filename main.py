  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Difference:", set(list1) - set(list2))