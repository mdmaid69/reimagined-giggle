import json
def convert_to_json(data):
        return json.dumps(data)
  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"