import sys
def print_python_version():
        print(sys.version)
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time