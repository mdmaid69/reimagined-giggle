numbers = [1, 2, 3, 4, 5]
print("Squared:", [n**2 for n in numbers])
import logging
def setup_logging(level):
        logging.basicConfig(level=level)