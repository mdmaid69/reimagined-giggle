import os
def remove_directory(path):
        os.rmdir(path)
def find_common_elements(list1, list2):
        return set(list1) & set(list2)