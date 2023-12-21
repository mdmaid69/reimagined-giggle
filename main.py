  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")