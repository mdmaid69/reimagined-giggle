import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import math
def calculate_circle_circumference(radius):
        return 2 * math.pi * radius