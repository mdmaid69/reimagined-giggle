import os
def change_working_directory(path):
        os.chdir(path)
def find_common_elements(list1, list2):
        return set(list1) & set(list2)