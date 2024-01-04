def is_prime(n):
        if n < 2: return False
        for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
                return False
        return True
import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))