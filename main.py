import json
def convert_to_json(data):
        return json.dumps(data)
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))