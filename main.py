  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
import collections
def count_elements(iterable):
        return collections.Counter(iterable)