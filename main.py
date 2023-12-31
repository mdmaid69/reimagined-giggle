import os
print(os.getcwd())
import logging
def setup_logging(level):
        logging.basicConfig(level=level)