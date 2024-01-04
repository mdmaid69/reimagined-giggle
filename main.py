import logging
def setup_logging(level):
        logging.basicConfig(level=level)
  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"