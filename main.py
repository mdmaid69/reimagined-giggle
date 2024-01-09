import logging
def setup_logging(level):
        logging.basicConfig(level=level)
def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets