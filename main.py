import os
def change_working_directory(path):
        os.chdir(path)
def remove_duplicates(lst):
        return list(set(lst))