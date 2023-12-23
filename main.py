import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
def calculate_roi(gain, cost):
        return (gain - cost) / cost