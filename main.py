import platform
def get_os_info():
        return platform.uname()
import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)