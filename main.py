list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Common elements:", set(list1) & set(list2))
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)