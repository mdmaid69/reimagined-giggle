import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
  def remove_duplicates(lst):
        return list(set(lst))