import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"