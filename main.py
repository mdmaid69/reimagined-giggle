def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
import os
def get_file_size(filename):
        return os.path.getsize(filename)