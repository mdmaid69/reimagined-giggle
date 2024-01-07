import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()