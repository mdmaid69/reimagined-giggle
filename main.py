import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
def find_union(list1, list2):
        return set(list1) | set(list2)