  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"
import logging
def setup_logging(level):
        logging.basicConfig(level=level)