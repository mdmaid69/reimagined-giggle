  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))