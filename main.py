import os
def remove_directory(path):
        os.rmdir(path)
def remove_duplicates(lst):
        return list(set(lst))