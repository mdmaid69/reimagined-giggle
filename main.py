import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Common elements:", set(list1) & set(list2))