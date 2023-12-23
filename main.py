  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Difference:", set(list1) - set(list2))