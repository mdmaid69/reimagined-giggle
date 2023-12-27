import logging
def log_message(message):
        logging.info(message)
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"