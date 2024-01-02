import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
  def count_elements(lst):
        return len(lst)