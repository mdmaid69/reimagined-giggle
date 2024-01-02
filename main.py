import logging
def log_message(message):
        logging.info(message)
import random
def generate_random_sample(population, k):
        return random.sample(population, k)