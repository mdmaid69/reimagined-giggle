import logging
def setup_logging(level):
        logging.basicConfig(level=level)
  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)