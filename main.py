def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
import numpy as np
print(np.array([1, 2, 3]))