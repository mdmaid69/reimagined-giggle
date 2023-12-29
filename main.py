  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)