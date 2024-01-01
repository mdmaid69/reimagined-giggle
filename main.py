import platform
def get_python_version():
        return platform.python_version()
import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)