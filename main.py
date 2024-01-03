  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Difference:", set(list1) - set(list2))