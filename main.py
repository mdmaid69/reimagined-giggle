def calculate_roi(gain, cost):
        return (gain - cost) / cost
import os
def get_file_size(filename):
        return os.path.getsize(filename)