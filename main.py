  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"
import itertools
print(list(itertools.permutations([1, 2, 3])))