import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"