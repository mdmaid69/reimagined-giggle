sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))
  import json
  def convert_dict_to_json(d):
        return json.dumps(d)