  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"