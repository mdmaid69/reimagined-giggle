import getpass
def get_username():
        return getpass.getuser()
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)