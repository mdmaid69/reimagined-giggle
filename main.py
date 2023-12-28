  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"