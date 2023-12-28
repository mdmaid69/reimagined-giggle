import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)