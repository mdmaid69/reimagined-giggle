  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
import logging
def log_message(message):
        logging.info(message)