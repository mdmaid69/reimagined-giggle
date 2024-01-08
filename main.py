import platform
def get_os_info():
        return platform.uname()
import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)