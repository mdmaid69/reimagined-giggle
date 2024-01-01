  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)
import logging
def setup_logging(level):
        logging.basicConfig(level=level)