text = "Hello, world!"
print("Is palindrome:", text == text[::-1])
  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)