  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)
import sklearn.datasets
print(sklearn.datasets.load_iris())