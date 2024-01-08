def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))