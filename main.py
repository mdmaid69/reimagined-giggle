  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))