import platform
def get_os_info():
        return platform.uname()
import math
def calculate_polar_to_cartesian_coordinates(r, theta):
        return math.polar((r, theta))