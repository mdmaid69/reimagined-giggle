import os
def get_file_size(filename):
        return os.path.getsize(filename)
def calculate_perpetuity(payment, rate):
        return payment / rate