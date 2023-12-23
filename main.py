import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import math
def calculate_cylinder_volume(radius, height):
        return math.pi * radius**2 * height