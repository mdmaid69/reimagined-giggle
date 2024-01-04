  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Common elements:", set(list1) & set(list2))