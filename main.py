import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [4, 5, 6])
plt.show()
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)