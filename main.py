import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))