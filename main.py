  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
import datetime
def get_current_date():
        return datetime.date.today()