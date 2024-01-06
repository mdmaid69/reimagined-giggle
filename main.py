import logging
def setup_logging(level):
        logging.basicConfig(level=level)
def calculate_profit_margin(revenue, cost):
        return (revenue - cost) / revenue