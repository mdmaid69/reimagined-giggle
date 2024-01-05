import json
print(json.dumps({"name": "John", "age": 30}))
  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)