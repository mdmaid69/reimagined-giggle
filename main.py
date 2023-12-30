import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
def calculate_perpetuity(payment, rate):
        return payment / rate