sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))
import json
def convert_to_json(data):
        return json.dumps(data)