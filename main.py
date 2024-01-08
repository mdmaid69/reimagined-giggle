import logging
def setup_logging(level):
        logging.basicConfig(level=level)
  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)