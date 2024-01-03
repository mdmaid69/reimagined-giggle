import logging
def setup_logging(level):
        logging.basicConfig(level=level)
def calculate_return_on_assets(net_income, total_assets):
        return net_income / total_assets