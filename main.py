import logging
def setup_logging(level):
        logging.basicConfig(level=level)
  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"