  import numpy as np
  def calculate_standard_deviation(arr):
        return np.std(arr)
def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b