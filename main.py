  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
  import datetime
  def get_current_date():
        return datetime.datetime.now().date()