  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)