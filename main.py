  import numpy as np
  def calculate_variance(arr):
        return np.var(arr)
import logging
def setup_logging(level):
        logging.basicConfig(level=level)