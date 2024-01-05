n = 10
print("Cube numbers:", [x**3 for x in range(n)])
import logging
def setup_logging(level):
        logging.basicConfig(level=level)