  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"
import json
def convert_to_json(data):
        return json.dumps(data)