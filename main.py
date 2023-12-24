def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")