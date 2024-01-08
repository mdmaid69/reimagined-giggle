  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
text = "Hello, world!"
print("Words:", len(text.split()))