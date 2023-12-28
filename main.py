  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))