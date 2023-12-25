import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import math
def calculate_circle_area(radius):
        return math.pi * radius**2