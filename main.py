import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3