import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)