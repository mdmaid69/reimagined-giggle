import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
  import time
  def wait_for_seconds(seconds):
        time.sleep(seconds)