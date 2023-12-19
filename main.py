import sys
def print_python_version():
        print(sys.version)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)