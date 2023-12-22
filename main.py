import logging
def setup_logging(level):
        logging.basicConfig(level=level)
def calculate_current_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities