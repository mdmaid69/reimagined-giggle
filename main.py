import os
def get_file_size(filename):
        return os.path.getsize(filename)
def find_union(list1, list2):
        return set(list1) | set(list2)