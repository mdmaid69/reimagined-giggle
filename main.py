import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
import random
def generate_random_sample(population, k):
        return random.sample(population, k)