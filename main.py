import os
def remove_directory(path):
        os.rmdir(path)
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Difference:", set(list1) - set(list2))