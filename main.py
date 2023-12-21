import os
def list_files_in_directory(path):
        return os.listdir(path)
def remove_duplicates(lst):
        return list(set(lst))