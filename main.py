numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])
  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)