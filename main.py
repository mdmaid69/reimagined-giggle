import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
import logging
def log_message(message):
        logging.info(message)