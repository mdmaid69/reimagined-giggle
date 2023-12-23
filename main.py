import logging
def setup_logging(level):
        logging.basicConfig(level=level)
def calculate_power(work, time):
        return work / time