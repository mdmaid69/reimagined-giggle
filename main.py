  import os
  def get_file_dev(file_name):
        return os.stat(file_name).st_dev
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Union:", set(list1) | set(list2))