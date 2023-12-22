import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal