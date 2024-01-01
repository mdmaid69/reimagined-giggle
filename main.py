import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()