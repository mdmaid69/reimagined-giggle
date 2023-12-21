import datetime
print(datetime.datetime.now())
import logging
def setup_logging(level):
        logging.basicConfig(level=level)