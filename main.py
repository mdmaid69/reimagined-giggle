import math
def calculate_polar_to_cartesian_coordinates(r, theta):
        return math.polar((r, theta))
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())