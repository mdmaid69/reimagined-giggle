import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
  import json
  def convert_dict_to_json(d):
        return json.dumps(d)