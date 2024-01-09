  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)