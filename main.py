def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)
import sys
def add_to_python_path(path):
        sys.path.append(path)