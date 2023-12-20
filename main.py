  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")