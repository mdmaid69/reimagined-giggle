  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
import datetime
def get_days_until_next_year():
        next_year = datetime.date.today().year + 1
        next_new_year = datetime.date(next_year, 1, 1)
        return (next_new_year - datetime.date.today()).days