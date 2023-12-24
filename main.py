import logging
def setup_logging(level):
        logging.basicConfig(level=level)
def calculate_perpetuity(payment, rate):
        return payment / rate