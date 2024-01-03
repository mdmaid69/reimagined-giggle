  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
def find_difference(list1, list2):
        return set(list1) - set(list2)