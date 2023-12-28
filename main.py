import os
def list_files_in_directory(path):
        return os.listdir(path)
def find_common_elements(list1, list2):
        return set(list1) & set(list2)