import logging
def setup_logging(level):
        logging.basicConfig(level=level)
def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)