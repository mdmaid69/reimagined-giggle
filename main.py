import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities