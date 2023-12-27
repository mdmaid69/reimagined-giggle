import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height