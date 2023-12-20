import sys
def add_to_python_path(path):
        sys.path.append(path)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)