list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Union:", set(list1) | set(list2))
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)