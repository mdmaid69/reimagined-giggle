import logging
def log_message(message):
        logging.info(message)
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps