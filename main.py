  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)