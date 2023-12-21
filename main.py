import sys
def add_to_python_path(path):
        sys.path.append(path)
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time