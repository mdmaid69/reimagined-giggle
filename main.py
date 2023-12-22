import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)