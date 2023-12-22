def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
import os
def list_files_in_directory(path):
        return os.listdir(path)