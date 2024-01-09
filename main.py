  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"
import json
def convert_to_json(data):
        return json.dumps(data)