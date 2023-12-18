import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
def find_unique_words(sentence):
        return set(sentence.split())