def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
import os
def remove_directory(path):
        os.rmdir(path)