  import numpy as np
  def create_numpy_array(lst):
        return np.array(lst)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)