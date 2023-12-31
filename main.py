import sys
def print_python_version():
        print(sys.version)
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time