import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))