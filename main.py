import logging
def log_message(message):
        logging.info(message)
  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"