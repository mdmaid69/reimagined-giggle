import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
def count_words(sentence):
        return len(sentence.split())