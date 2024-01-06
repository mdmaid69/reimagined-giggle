import os
def change_working_directory(path):
        os.chdir(path)
def calculate_perpetuity(payment, rate):
        return payment / rate