  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
import re
def split_string(pattern, string):
        return re.split(pattern, string)