  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"
import json
def read_from_json(json_string):
        return json.loads(json_string)