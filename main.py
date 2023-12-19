import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
import logging
def setup_logging(level):
        logging.basicConfig(level=level)