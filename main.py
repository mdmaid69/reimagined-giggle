list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Difference:", set(list1) - set(list2))
  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)