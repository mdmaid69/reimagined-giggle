def find_difference(list1, list2):
        return set(list1) - set(list2)
import os
def remove_directory(path):
        os.rmdir(path)