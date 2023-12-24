import logging
def setup_logging(level):
        logging.basicConfig(level=level)
def calculate_average(numbers):
        return sum(numbers) / len(numbers)