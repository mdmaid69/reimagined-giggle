def find_unique_words(sentence):
        return set(sentence.split())
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)