  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)