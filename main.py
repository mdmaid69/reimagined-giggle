import logging
def setup_logging(level):
        logging.basicConfig(level=level)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))