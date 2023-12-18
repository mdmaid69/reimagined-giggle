  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Difference:", set(list1) - set(list2))