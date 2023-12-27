import os
def remove_directory(path):
        os.rmdir(path)
def calculate_perpetuity(payment, rate):
        return payment / rate