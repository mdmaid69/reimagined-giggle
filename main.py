import math
def calculate_cylinder_volume(radius, height):
        return math.pi * radius**2 * height
import os
def get_environment_variable(var):
        return os.getenv(var)