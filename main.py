import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
def find_union(list1, list2):
        return set(list1) | set(list2)