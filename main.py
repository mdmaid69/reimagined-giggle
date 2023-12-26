  import os
  def delete_file(file_name):
        os.remove(file_name)
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Union:", set(list1) | set(list2))