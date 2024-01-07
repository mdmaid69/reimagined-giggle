  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))