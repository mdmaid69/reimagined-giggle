import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)