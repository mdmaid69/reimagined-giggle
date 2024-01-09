import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
import datetime
def get_current_date():
        return datetime.date.today()