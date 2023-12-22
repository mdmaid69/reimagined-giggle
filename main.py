import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())