def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)