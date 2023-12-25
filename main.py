sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)