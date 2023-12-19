import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
  def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)