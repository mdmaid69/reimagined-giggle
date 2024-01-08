  def reverse_list(lst):
        return lst[::-1]
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))