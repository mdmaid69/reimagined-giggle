import logging
def setup_logging(level):
        logging.basicConfig(level=level)
import random
def generate_random_number(start, end):
        return random.randint(start, end)