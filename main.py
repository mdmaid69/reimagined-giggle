import platform
def get_os_info():
        return platform.uname()
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)