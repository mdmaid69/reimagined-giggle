import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
import numpy as np
print(np.array([1, 2, 3]))