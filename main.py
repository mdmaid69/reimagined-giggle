import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)