list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Common elements:", set(list1) & set(list2))
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)