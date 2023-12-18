  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)