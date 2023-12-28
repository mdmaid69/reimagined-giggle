  def convert_to_binary(n):
        return bin(n)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))