  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)