import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)