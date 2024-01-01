sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))
import json
def read_from_json(json_string):
        return json.loads(json_string)