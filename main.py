import os
def get_environment_variable(var):
        return os.getenv(var)
import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height