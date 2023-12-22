  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"
import json
def read_from_json(json_string):
        return json.loads(json_string)