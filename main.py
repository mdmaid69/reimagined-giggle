  import os
  def get_current_working_directory():
        return os.getcwd()
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Difference:", set(list1) - set(list2))