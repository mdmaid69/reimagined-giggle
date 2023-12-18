  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))