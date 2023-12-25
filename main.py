import random
def roll_die():
        return random.randint(1, 6)
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()