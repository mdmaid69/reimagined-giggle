  def calculate_area_circle(r):
        return 3.14 * r**2
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)