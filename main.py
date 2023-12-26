  def calculate_area_rectangle(l, w):
        return l * w
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)