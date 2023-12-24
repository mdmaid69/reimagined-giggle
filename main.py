import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
  def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)