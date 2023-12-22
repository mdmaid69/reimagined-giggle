def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
import logging
def setup_logging(level):
        logging.basicConfig(level=level)