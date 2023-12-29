  import numpy as np
  def calculate_median(arr):
        return np.median(arr)
def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b