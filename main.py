  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))