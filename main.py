def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities
import logging
def setup_logging(level):
        logging.basicConfig(level=level)