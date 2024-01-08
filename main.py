import sys
def add_to_python_path(path):
        sys.path.append(path)
def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal