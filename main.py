  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Common elements:", set(list1) & set(list2))