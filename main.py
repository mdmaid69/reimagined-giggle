import logging
def setup_logging(level):
        logging.basicConfig(level=level)
import random
def generate_random_choice(choices):
        return random.choice(choices)