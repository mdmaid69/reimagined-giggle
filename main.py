sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)