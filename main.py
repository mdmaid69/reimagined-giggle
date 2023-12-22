sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)