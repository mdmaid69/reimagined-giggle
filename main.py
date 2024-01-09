import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
def find_difference(list1, list2):
        return set(list1) - set(list2)