n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])
import logging
def setup_logging(level):
        logging.basicConfig(level=level)