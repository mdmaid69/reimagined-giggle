import platform
def get_os_info():
        return platform.uname()
import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)