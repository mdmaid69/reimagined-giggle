import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
import random
def roll_die():
        return random.randint(1, 6)