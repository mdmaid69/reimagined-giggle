import random
def generate_random_number(start, end):
        return random.randint(start, end)
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()