def calculate_average(lst):
        return sum(lst) / len(lst)
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)