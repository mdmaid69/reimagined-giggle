import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))