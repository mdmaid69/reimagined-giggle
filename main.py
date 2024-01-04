import sys
def exit_program():
        sys.exit()
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)