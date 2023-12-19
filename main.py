import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3