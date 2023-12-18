  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")