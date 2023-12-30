  def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)