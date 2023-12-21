import json
def read_from_json(json_string):
        return json.loads(json_string)
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))