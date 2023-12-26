import logging
def setup_logging(level):
        logging.basicConfig(level=level)
def is_odd(n):
        return n % 2 != 0