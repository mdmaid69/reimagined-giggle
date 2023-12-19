n = 10
print("Powers of 2:", [2**x for x in range(n)])
import logging
def setup_logging(level):
        logging.basicConfig(level=level)