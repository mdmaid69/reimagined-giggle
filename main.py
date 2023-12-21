import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
  def calculate_area_triangle(b, h):
        return 0.5 * b * h