  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"