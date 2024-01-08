  import os
  def get_file_atime_ns(file_name):
        return os.stat(file_name).st_atime_ns
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Union:", set(list1) | set(list2))