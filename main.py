import logging
def setup_logging(level):
        logging.basicConfig(level=level)
  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)