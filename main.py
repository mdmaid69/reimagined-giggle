import datetime
def get_current_datetime():
        return datetime.datetime.now()
  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)