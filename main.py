def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)