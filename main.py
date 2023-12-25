  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Union:", set(list1) | set(list2))