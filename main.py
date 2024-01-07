def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
import logging
def setup_logging(level):
        logging.basicConfig(level=level)