import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import random
def generate_random_choice(choices):
        return random.choice(choices)