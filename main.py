import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import numpy as np
print(np.array([1, 2, 3]))