  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))