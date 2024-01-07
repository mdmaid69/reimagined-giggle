n = 10
print("Square numbers:", [x**2 for x in range(n)])
import logging
def setup_logging(level):
        logging.basicConfig(level=level)