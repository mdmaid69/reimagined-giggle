import numpy as np
print(np.array([1, 2, 3]))
def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)