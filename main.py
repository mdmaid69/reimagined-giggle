import math
def calculate_sign(x):
        return math.copysign(1, x)
import platform
def get_os_info():
        return platform.uname()