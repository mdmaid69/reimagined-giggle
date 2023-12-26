import datetime
def get_today_date():
        return datetime.date.today()
  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)