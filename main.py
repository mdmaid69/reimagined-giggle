import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
import math
def calculate_cylinder_volume(radius, height):
        return math.pi * radius**2 * height