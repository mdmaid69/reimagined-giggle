list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Union:", set(list1) | set(list2))
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)