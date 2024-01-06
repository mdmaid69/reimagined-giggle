import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
import random
def generate_random_choice(choices):
        return random.choice(choices)