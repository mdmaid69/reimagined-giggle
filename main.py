import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps