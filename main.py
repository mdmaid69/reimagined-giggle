  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")