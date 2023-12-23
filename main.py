import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)