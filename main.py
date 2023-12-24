import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
def find_unique_words(sentence):
        return set(sentence.split())