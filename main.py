  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)