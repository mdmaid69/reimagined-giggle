n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))
  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)