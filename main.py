import logging
def setup_logging(level):
        logging.basicConfig(level=level)
import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list