import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")