import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"