  def remove_duplicates(lst):
        return list(set(lst))
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))