import random
def generate_random_sample(population, k):
        return random.sample(population, k)
import logging
def setup_logging(level):
        logging.basicConfig(level=level)