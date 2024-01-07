import logging
def setup_logging(level):
        logging.basicConfig(level=level)
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"