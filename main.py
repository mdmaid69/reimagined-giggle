import sys
print(sys.version)
import logging
def setup_logging(level):
        logging.basicConfig(level=level)