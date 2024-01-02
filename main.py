def count_words(sentence):
        return len(sentence.split())
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)