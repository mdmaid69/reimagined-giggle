import os
def change_working_directory(path):
        os.chdir(path)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)