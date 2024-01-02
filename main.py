import logging
def setup_logging(level):
        logging.basicConfig(level=level)
def calculate_simple_interest(principal, rate, time):
        return principal * rate * time