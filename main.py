import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
def count_elements(lst):
        return len(lst)