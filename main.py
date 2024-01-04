def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
import sys
def add_to_python_path(path):
        sys.path.append(path)