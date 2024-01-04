import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)