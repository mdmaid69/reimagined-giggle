import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))