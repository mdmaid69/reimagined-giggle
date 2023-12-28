import random
def generate_random_sample(population, k):
        return random.sample(population, k)
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")