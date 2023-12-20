import logging
def setup_logging(level):
        logging.basicConfig(level=level)
def calculate_roi(gain, cost):
        return (gain - cost) / cost