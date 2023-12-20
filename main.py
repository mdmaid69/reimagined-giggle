import logging
def setup_logging(level):
        logging.basicConfig(level=level)
def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)