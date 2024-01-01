def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
import numpy as np
print(np.array([1, 2, 3]))