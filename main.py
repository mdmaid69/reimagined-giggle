n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])
import logging
def setup_logging(level):
        logging.basicConfig(level=level)