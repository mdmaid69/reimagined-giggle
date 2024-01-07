import logging
def setup_logging(level):
        logging.basicConfig(level=level)
def calculate_eps(net_income, shares_outstanding):
        return net_income / shares_outstanding