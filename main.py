def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps
import logging
def setup_logging(level):
        logging.basicConfig(level=level)