def calculate_roi(gain, cost):
        return (gain - cost) / cost
import logging
def setup_logging(level):
        logging.basicConfig(level=level)