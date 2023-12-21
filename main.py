import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
import logging
def log_message(message):
        logging.info(message)