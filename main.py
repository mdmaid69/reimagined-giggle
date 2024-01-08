import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())