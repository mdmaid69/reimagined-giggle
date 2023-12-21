  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
import collections
def create_queue():
        return collections.deque()