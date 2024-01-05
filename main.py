import time
def get_current_time():
        return time.ctime()
import random
def generate_random_sample(population, k):
        return random.sample(population, k)