import logging
def setup_logging(level):
        logging.basicConfig(level=level)
n = 10
print("Fibonacci:", [((1 + 5**0.5) / 2)**n / 5**0.5 for n in range(n)])