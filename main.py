list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Difference:", set(list1) - set(list2))
  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)