  import numpy as np
  def create_numpy_array(lst):
        return np.array(lst)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)