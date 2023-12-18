import random
def roll_die():
        return random.randint(1, 6)
import logging
def setup_logging(level):
        logging.basicConfig(level=level)