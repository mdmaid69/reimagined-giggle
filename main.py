import logging
def setup_logging(level):
        logging.basicConfig(level=level)
def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal