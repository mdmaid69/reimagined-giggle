  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
  import time
  def wait_for_seconds(seconds):
        time.sleep(seconds)