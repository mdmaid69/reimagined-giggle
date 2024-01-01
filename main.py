import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [4, 5, 6])
plt.show()
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)