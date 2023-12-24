import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))