import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"